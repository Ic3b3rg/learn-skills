# Run with: ruby scripts/validate_skills.rb
require 'yaml'
require 'json'
require 'pathname'

root = Pathname.new(__dir__).parent
errors = []
skills = root.join('skills').children.select(&:directory?).sort
errors << 'No skills found' if skills.empty?
metadata_by_name = {}
skills.each do |dir|
  path = dir.join('SKILL.md')
  unless path.file?
    errors << "#{dir.basename}: SKILL.md is missing"
    next
  end
  text = path.read
  frontmatter = text.match(/\A---\r?\n(.*?)\r?\n---(?:\r?\n|\z)/m)
  begin
    data = frontmatter && YAML.safe_load(frontmatter[1])
    raise 'Frontmatter must be a mapping' unless data.is_a?(Hash)
    metadata_by_name[dir.basename.to_s] = data
    name = data['name']
    raise 'Name must match its directory' unless name == dir.basename.to_s
    raise 'Invalid name' unless name.size <= 64 && name.match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\z/)
    description = data['description']
    raise 'Invalid description' unless description.is_a?(String) && !description.strip.empty? && description.size <= 1024 && !description.match?(/[<>]/)
    raise 'Local 100-line cap exceeded' if text.lines.size > 100
  rescue StandardError => e
    errors << "#{path.relative_path_from(root)}: #{e.message}"
  end

  dir.glob('**/*.md').each do |file|
    # Template examples contain placeholder links, not resource dependencies.
    prose = file.read.gsub(/^```[^\n]*\n.*?^```[^\n]*(?:\n|\z)/m, '')
    prose.scan(/\]\(([^)]+)\)/).flatten.each do |target|
      next if target.match?(/\A(?:[a-z][a-z0-9+.-]*:|#)/i)
      resolved = file.dirname.join(target.split('#').first).cleanpath
      inside = resolved.to_s.start_with?(dir.to_s + '/')
      errors << "#{file.relative_path_from(root)}: resource escapes skill: #{target}" unless inside
      errors << "#{file.relative_path_from(root)}: missing resource: #{target}" unless resolved.exist?
    end
  end

  policy = dir.join('SOURCES.md')
  errors << "#{dir.basename}: bundled source policy missing or stale" unless policy.exist? && policy.read == root.join('docs/sources.md').read
  unless text.include?('[SOURCES.md](SOURCES.md)')
    errors << "#{dir.basename}: entrypoint must link bundled source policy"
  end

  metadata = dir.join('agents/openai.yaml')
  if metadata.exist?
    begin
      ui = YAML.safe_load(metadata.read)
      prompt = ui.fetch('interface').fetch('default_prompt')
      raise 'Default prompt must invoke this skill' unless prompt.include?("$#{dir.basename}")
      raise 'Automatic routing is disabled' if ui.fetch('policy', {})['allow_implicit_invocation'] == false
    rescue StandardError => e
      errors << "#{metadata.relative_path_from(root)}: #{e.message}"
    end
  end
end

flows = root.join('skills/start-learn/FLOWS.md')
if flows.file?
  targets = flows.read.scan(/^\|[^\n]+\| `\/([a-z0-9-]+)\b/).flatten.uniq
  errors << 'start-learn: no router targets found' if targets.empty?
  targets.each do |name|
    target = metadata_by_name[name]
    if target.nil?
      errors << "start-learn: router target #{name} is not installed"
    elsif target['disable-model-invocation'] == true
      errors << "start-learn: router target #{name} disables model invocation"
    end
  end
else
  errors << 'start-learn: FLOWS.md is missing'
end

%w[.claude-plugin/plugin.json .claude-plugin/marketplace.json .codex-plugin/plugin.json .agents/plugins/marketplace.json].each do |file|
  begin
    JSON.parse(root.join(file).read)
  rescue StandardError => e
    errors << "#{file}: #{e.message}"
  end
end

abort errors.join("\n") unless errors.empty?
puts "Validated #{skills.size} skills: YAML, names, descriptions, local line cap, self-contained Markdown resources, source-policy copies, router targets, UI metadata and JSON syntax."
