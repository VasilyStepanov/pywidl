<%!
  import pywidl
%>
<%def name="emitAttribute(attribute)"><%
  specifier = "attribute"
  if attribute.readonly: specifier = "readonly %s" % specifier
  if attribute.inherit: specifier = "inherit %s" % specifier
%>  ${specifier} ${attribute.type} ${attribute.name};
</%def>
<%def name="emitInterfaceMember(member)">
% if isinstance(member, pywidl.Attribute):
${emitAttribute(member)}
% else:
// unknown interface member ${type(member)}
% endif
</%def>
<%def name="emitInterface(interface)"><%
  if interface.parent:
    declaration = "%s : %s" % (interface.name, interface.parent)
  else:
    declaration = "%s" % interface.name
%>interface ${declaration} {
% for member in interface.members:
${emitInterfaceMember(member)}
% endfor
};
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
