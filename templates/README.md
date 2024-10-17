# Project Management Templates

This folder contains a collection of TOML-based project management templates designed to streamline various aspects of project planning, execution, and monitoring. These templates are used by the AI Hacker League Project Management System to create standardized issues and documents for efficient project management.

## Table of Contents

1. [Available Templates](#available-templates)
2. [How to Use Templates](#how-to-use-templates)
3. [Creating Custom Templates](#creating-custom-templates)
4. [Template Structure](#template-structure)
5. [Best Practices](#best-practices)

## Available Templates

1. **Bug Report** (bug_report.toml)
   - Purpose: To report and track software bugs or issues
   - Key fields: Bug title, description, steps to reproduce, expected behavior, actual behavior

2. **Change Request** (change_request.toml)
   - Purpose: To propose and track changes to the project scope, timeline, or resources
   - Key fields: Change title, description, justification, impact assessment, risk assessment

3. **Dependency Tracking** (dependency_tracking.toml)
   - Purpose: To identify and manage project dependencies
   - Key fields: Dependency name, type, description, required by date, impact if not met

4. **Epic** (epic.toml)
   - Purpose: To define and track large, high-level user stories or features
   - Key fields: Epic title, description, business value, user stories, estimated timeline

5. **Feature Request** (feature_request.toml)
   - Purpose: To propose and track new feature ideas
   - Key fields: Feature title, description, use case, proposed solution, alternatives

6. **Meeting Minutes** (meeting_minutes.toml)
   - Purpose: To record discussions, decisions, and action items from project meetings
   - Key fields: Meeting title, date, attendees, agenda, discussion points, action items

7. **Milestone** (milestone.toml)
   - Purpose: To define and track significant project checkpoints or deliverables
   - Key fields: Milestone name, due date, description, deliverables, success criteria

8. **Project Charter** (project_charter.toml)
   - Purpose: To formally authorize and define the scope of a project
   - Key fields: Project name, overview, objectives, scope, stakeholders, timeline, budget

9. **Project Status Report** (project_status_report.toml)
   - Purpose: To provide regular updates on project progress, issues, and metrics
   - Key fields: Project name, overall status, key accomplishments, issues/risks, budget status

10. **Quality Assurance** (quality_assurance.toml)
    - Purpose: To define and track quality assurance activities and criteria
    - Key fields: QA item name, type, description, quality criteria, testing methodology

11. **Resource Allocation** (resource_allocation.toml)
    - Purpose: To plan and track the allocation of team members and resources
    - Key fields: Resource name, role, current assignments, availability, skills/expertise

12. **Retrospective** (retrospective.toml)
    - Purpose: To facilitate team reflection and improvement after each sprint or project phase
    - Key fields: Sprint number, what went well, what needs improvement, action items

13. **Risk Assessment** (risk_assessment.toml)
    - Purpose: To identify, evaluate, and plan mitigation strategies for project risks
    - Key fields: Risk title, description, probability, impact, mitigation strategy

14. **Sprint Planning** (sprint_planning.toml)
    - Purpose: To plan and define the goals and tasks for an upcoming sprint
    - Key fields: Sprint number, goal, duration, team capacity, sprint backlog

15. **Stakeholder Analysis** (stakeholder_analysis.toml)
    - Purpose: To identify and analyze project stakeholders and their interests
    - Key fields: Stakeholder name, role, interest level, influence level, communication strategy

16. **Task** (task.toml)
    - Purpose: To define and track individual work items or tasks
    - Key fields: Task title, description, acceptance criteria, estimated effort

17. **User Story** (user_story.toml)
    - Purpose: To capture user requirements in an agile development process
    - Key fields: Story title, user type, desired action, benefit, acceptance criteria

## How to Use Templates

1. **Via API**: Use the `/templates/` endpoint to list all available templates and their details.

2. **Applying Templates**: When creating a new issue or document, specify the template name to use. The system will automatically populate the fields based on the chosen template.

3. **Customizing Instances**: After applying a template, you can modify the pre-filled fields to suit your specific needs.

4. **Updating Templates**: If you need to make changes to a template, update the corresponding TOML file and restart the application to reload the templates.

## Creating Custom Templates

To create a custom template:

1. Create a new TOML file in the `templates/` directory with a descriptive name (e.g., `my_custom_template.toml`).

2. Follow the template structure outlined below.

3. Define the title, body, and fields for your template.

4. Restart the application to load the new template.

## Template Structure

Each template follows this general structure:

```toml
title = "Template Title: {variable}"

body = """
## Section 1
{field1}

## Section 2
{field2}

...
"""

[fields]
variable = { type = "string", required = true }
field1 = { type = "string", required = true }
field2 = { type = "integer", required = false }
...
```

- `title`: Defines the template title, which can include variables in curly braces.
- `body`: The main content of the template, using Markdown formatting. Variables are enclosed in curly braces.
- `[fields]`: Defines the properties of each field used in the title and body.
  - `type`: Can be "string", "integer", "float", "boolean", or "date".
  - `required`: Set to `true` if the field must be filled, `false` if it's optional.

## Best Practices

1. **Use Descriptive Names**: Choose clear and descriptive names for your templates and fields.

2. **Provide Context**: Include instructions or examples in the template body to guide users.

3. **Use Markdown**: Utilize Markdown formatting in the body to improve readability.

4. **Keep it Concise**: While being comprehensive, avoid unnecessary verbosity in your templates.

5. **Consistent Formatting**: Maintain consistent formatting across all templates for a unified experience.

6. **Regular Reviews**: Periodically review and update templates to ensure they remain relevant and effective.

7. **Version Control**: Keep your templates under version control to track changes over time.

8. **Documentation**: Always update this README when adding new templates or making significant changes.

By following these guidelines and utilizing the provided templates, you can ensure consistent and efficient project management practices across your projects.
