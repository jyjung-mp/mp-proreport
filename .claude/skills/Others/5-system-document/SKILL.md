---
name: system-documentation
description: This skill should be used when users want to document system architecture, technical workflows, or service flows in a structured wiki format. Use this skill when the user requests system documentation, architecture documentation, or wants to create/update technical documentation in Confluence wiki.
---

# System Documentation

## Overview

This skill provides a structured workflow for documenting system architectures, technical processes, and service flows in Confluence wiki format. It guides the documentation process from information gathering to creating comprehensive, well-structured wiki pages with diagrams and detailed explanations.

## When to Use This Skill

Use this skill when the user wants to:
- Document a new or existing system architecture
- Create technical documentation for service flows or processes
- Update existing wiki pages with system structure information
- Visualize system workflows with diagrams
- Organize technical information in a structured format

Typical user requests include:
- "Help me document the payment system architecture"
- "I need to create wiki documentation for our new API service"
- "Document this authentication flow on the wiki"

## Documentation Workflow

### Step 1: Information Gathering

Before creating documentation, gather all necessary information by asking targeted questions. The documentation requires five key pieces of information:

1. **Service Description**
   - What is this system/service?
   - What problem does it solve?
   - What are the main features?

2. **Related Resources**
   - Jira issue keys or URLs
   - Existing wiki page URLs
   - Planning documents or reference materials
   - Related documentation links

3. **Environment Information**
   - Domain names (production, staging, development)
   - Server names and infrastructure details
   - API endpoints
   - Database information
   - External service dependencies

4. **Process Flow**
   - Step-by-step workflow description
   - Data flow between components
   - Integration points with external systems
   - Error handling and fallback procedures
   - Scheduling information (if applicable)

5. **Target Wiki Page**
   - Which wiki page should be updated?
   - Ask for the wiki page ID or URL
   - If creating a new page, ask for parent page information

**Important:** If any information is missing or unclear, ask specific questions to gather complete details. Do not proceed with incomplete information.

### Step 2: Choose Diagram Type

Based on the system characteristics, select the appropriate diagram type:

**Sequence Diagram** - Use when:
- Showing interactions between multiple components/services
- Timing and order of operations are important
- Request-response patterns need to be illustrated
- Multiple actors or services communicate

**Activity Diagram** - Use when:
- Showing a workflow or process flow
- Decision points and conditional logic exist
- Parallel processing needs to be shown
- Focus is on the flow of control

**Component Diagram** - Use when:
- Showing system architecture and structure
- Illustrating relationships between components
- Highlighting deployment architecture

All diagrams should be created using PlantUML syntax for Confluence integration.

### Step 3: Create Document Structure

Organize the documentation using the following standard structure:

#### 1. Title and Overview
```html
<h1><strong>[System/Service Name]</strong></h1>

<ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="[generate-uuid]">
  <ac:rich-text-body>
    <p>[Brief description of the system/service]</p>
  </ac:rich-text-body>
</ac:structured-macro>
```

#### 2. Diagram Section
```html
<h2><strong>[Diagram Title]</strong></h2>

<ac:structured-macro ac:name="plantuml" ac:schema-version="1" ac:macro-id="[generate-uuid]">
  <ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter>
  <ac:plain-text-body><![CDATA[
@startuml
[PlantUML diagram code]
@enduml
]]></ac:plain-text-body>
</ac:structured-macro>
```

#### 3. Flow Details
```html
<h2><strong>플로우 상세 설명</strong></h2>

<h3><strong>[Phase/Stage Name]</strong></h3>

<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="[generate-uuid]">
  <ac:parameter ac:name="bgColor">#DEEBFF</ac:parameter>
  <ac:parameter ac:name="borderStyle">solid</ac:parameter>
  <ac:rich-text-body>
    <table class="wrapped">
      [Table content with steps]
    </table>
  </ac:rich-text-body>
</ac:structured-macro>
```

#### 4. Key Components
```html
<h2><strong>주요 구성 요소</strong></h2>

<table class="wrapped">
  <tbody>
    <tr>
      <th><strong>구성 요소</strong></th>
      <th><strong>설명</strong></th>
    </tr>
    [Component rows with status macros]
  </tbody>
</table>
```

#### 5. Additional Sections (as needed)
- Execution schedule/timeline
- Environment details
- API specifications
- Error handling procedures
- Monitoring and alerting

### Step 4: Generate Documentation

Create the complete documentation following these guidelines:

**Diagram Creation:**
- Use appropriate PlantUML syntax based on chosen diagram type
- Apply color coding for visual clarity (see `references/diagram_examples.md`)
- Include all system components and interactions
- Add notes for important details

**Content Writing:**
- Write clear, concise descriptions
- Use tables for structured information
- Apply Confluence macros (info, tip, panel, status) for visual enhancement
- Include code examples where relevant
- Add links to related resources (Jira, wiki, documents)

**Visual Consistency:**
- Use consistent color schemes (reference the sample pages)
- Apply status macros with appropriate colors
- Structure tables uniformly
- Use panel macros to highlight important sections

### Step 5: Update Wiki Page

Once documentation is complete:

1. **Verify Page Access:**
   - Confirm the target wiki page ID or URL
   - Check if the page exists and is accessible

2. **Update the Page:**
   - Use the wiki update tool to publish the documentation
   - For new sections, append to existing content
   - For updates, replace specific sections as requested

3. **Confirm with User:**
   - Provide the wiki page URL
   - Summarize what was documented
   - Ask if any adjustments are needed

## Resources

### references/

This skill includes reference documentation to assist with creating consistent, high-quality documentation:

- `confluence_templates.md` - Confluence macro templates and HTML structure examples
- `diagram_examples.md` - PlantUML diagram templates and color schemes

Load these references as needed when creating specific types of content or diagrams.

## Best Practices

1. **Always gather complete information before starting** - Incomplete information leads to poor documentation
2. **Choose the right diagram type** - The diagram should match the documentation purpose
3. **Be consistent with formatting** - Use the same structure and styling throughout
4. **Include links to related resources** - Connect to Jira issues, related wiki pages, and reference documents
5. **Make it visual** - Use diagrams, tables, and color coding to improve readability
6. **Keep it updated** - When updating existing pages, preserve important existing content