<%!
  import pywidl
%>
<%def name="emitInterface(interface)">
interface ${interface.name} { };
</%def>
<%def name="emitDefinition(definition)">
% if isinstance(definition, pywidl.Interface):
${emitInterface(definition)}
% else:
// unknown definition type ${type(definition)}
% endif
</%def>
source: ${source}
output: ${output}
template: ${template}
template_type: ${template_type}

% for definition in definitions:
${emitDefinition(definition)}
% endfor
