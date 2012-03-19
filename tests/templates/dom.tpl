<%!
  import pywidl
%><%def name="emitType(typedef)"><%
  if isinstance(typedef, pywidl.Any):
    specifier = "any"
  elif isinstance(typedef, pywidl.Array):
    specifier = "%s[]" % emitType(typedef.t)
  else:
    specifier = "/* unknown type %s */" % type(typedef)
  if getattr(typedef, "nullable", False):
    specifier = "%s?" % specifier
%>${specifier}</%def><%def name="emitAttribute(attribute)"><%
  specifier = "attribute"
  if attribute.readonly: specifier = "readonly %s" % specifier
  if attribute.inherit: specifier = "inherit %s" % specifier
%>  ${specifier} ${emitType(attribute.type)} ${attribute.name};</%def><%def name="emitInterfaceMember(member)"><%
  if isinstance(member, pywidl.Attribute):
    specifier = emitAttribute(member)
  else:
    specifier = "/* unknown interface member %s */" % type(member)
%>${specifier}</%def><%def name="emitInterface(interface)"><%
  if interface.parent:
    declaration = "%s : %s" % (interface.name, interface.parent)
  else:
    declaration = "%s" % interface.name
%>interface ${declaration} {
% for member in interface.members:
${emitInterfaceMember(member)}
% endfor
};</%def><%def name="emitDefinition(definition)"><%
  if isinstance(definition, pywidl.Interface):
    specifier = emitInterface(definition)
  else:
    specifier = "/* unknown definition type %s */" % type(definition)
%>${specifier}</%def>source: ${source}
output: ${output}
template: ${template}
template_type: ${template_type}
% for definition in definitions:



${emitDefinition(definition)}
% endfor
