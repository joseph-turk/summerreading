const requiredCheckboxes = $(':checkbox[required]')

requiredCheckboxes.change(() => {
  if (requiredCheckboxes.is(':checked')) { requiredCheckboxes.removeAttr('required') } else requiredCheckboxes.attr('required', 'required')
})
