<%!
  import pywidl
%>
<%def name="emitInterface(interface)">
<%
  if interface.parent:
    declaration = "%s : %s" % (interface.name, interface.parent)
  else:
    declaration = "%s" % interface.name
%>interface ${declaration} { };
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
