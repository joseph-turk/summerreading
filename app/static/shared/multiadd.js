// Function to add new child name input
function addChild () {
  let lastChild = document.getElementById(`childname${nextChild - 1}`)
  if (lastChild.value === '') {
    // Prevent adding another child if blank input is available
    lastChild.focus()
  } else {
    // Create horizontal rule element
    let hr = document.createElement('hr')
    hr.setAttribute('class', 'mt-3')
    childrenDiv.appendChild(hr)

    // Create elements for name form group
    let newChildDiv = document.createElement('div')
    let newChildLabel = document.createElement('label')
    let labelContent = document.createTextNode('Name (First and Last)')
    let newChildInput = document.createElement('input')

    // Set attributes on new elements
    newChildDiv.setAttribute('class', 'form-group')
    newChildLabel.setAttribute('for', `childname${nextChild}`)
    newChildLabel.appendChild(labelContent)
    newChildInput.setAttribute('class', 'form-control')
    newChildInput.setAttribute('id', `childname${nextChild}`)
    newChildInput.setAttribute('name', `childname${nextChild}`)
    newChildInput.setAttribute('required', '')

    // Build form-group div
    newChildDiv.appendChild(newChildLabel)
    newChildDiv.appendChild(newChildInput)

    // Append form-group to form
    childrenDiv.appendChild(newChildDiv)

    // Set focus in new input
    newChildInput.focus()

    // Create elements for photo consent
    let photoConsentDiv = document.createElement('div')
    let photoConsentYesDiv = document.createElement('div')
    let photoConsentNoDiv = document.createElement('div')
    let photoConsentLabel = document.createElement('label')
    let photoConsentYesLabel = document.createElement('label')
    let photoConsentNoLabel = document.createElement('label')
    let photoConsentLabelContent = document.createTextNode(
      'Can we take and use photographs of this child at library events?'
    )
    let photoConsentYesLabelContentStrong = document.createElement('strong')
    let photoConsentYesLabelDetailsSpan = document.createElement('span')
    let photoConsentYesLabelContent = document.createTextNode('Yes:')
    let photoConsentYesLabelDetails = document.createTextNode(
      'I hereby consent to the use of any photographs, video or audio clips of this child in news coverage or publicity for the Eager Free Public Library. This may include use in our newsletters, brochures, fliers, posters, and/or web pages.'
    )
    let photoConsentNoLabelContentStrong = document.createElement('strong')
    let photoConsentNoLabelDetailsSpan = document.createElement('span')
    let photoConsentNoLabelContent = document.createTextNode('No:')
    let photoConsentNoLabelDetails = document.createTextNode(
      'I do not consent to the use of photographs, video or audio clips of this child.'
    )
    let photoConsentYesInput = document.createElement('input')
    let photoConsentNoInput = document.createElement('input')

    // Set attributes for photo consent
    photoConsentDiv.setAttribute('class', 'form-group')
    photoConsentYesDiv.setAttribute('class', 'form-check')
    photoConsentNoDiv.setAttribute('class', 'form-check')
    photoConsentYesLabel.setAttribute('for', `consentyes${nextChild}`)
    photoConsentNoLabel.setAttribute('for', `consentno${nextChild}`)
    photoConsentYesLabel.setAttribute(
      'class',
      'form-check-label d-flex justify-content-between'
    )
    photoConsentNoLabel.setAttribute(
      'class',
      'form-check-label d-flex justify-content-between'
    )
    photoConsentLabel.appendChild(photoConsentLabelContent)
    photoConsentYesLabelContentStrong.setAttribute('class', 'mr-2')
    photoConsentNoLabelContentStrong.setAttribute('class', 'mr-2')
    photoConsentYesLabelContentStrong.appendChild(photoConsentYesLabelContent)
    photoConsentYesLabelDetailsSpan.appendChild(photoConsentYesLabelDetails)
    photoConsentYesLabel.appendChild(photoConsentYesLabelContentStrong)
    photoConsentYesLabel.appendChild(photoConsentYesLabelDetailsSpan)
    photoConsentNoLabelContentStrong.appendChild(photoConsentNoLabelContent)
    photoConsentNoLabelDetailsSpan.appendChild(photoConsentNoLabelDetails)
    photoConsentNoLabel.appendChild(photoConsentNoLabelContentStrong)
    photoConsentNoLabel.appendChild(photoConsentNoLabelDetailsSpan)
    photoConsentYesInput.setAttribute('class', 'form-check-input')
    photoConsentYesInput.setAttribute('type', 'radio')
    photoConsentYesInput.setAttribute('id', `consentyes${nextChild}`)
    photoConsentYesInput.setAttribute('name', `childphotorelease${nextChild}`)
    photoConsentYesInput.setAttribute('value', '1')
    photoConsentYesInput.setAttribute('required', '')
    photoConsentNoInput.setAttribute('class', 'form-check-input')
    photoConsentNoInput.setAttribute('type', 'radio')
    photoConsentNoInput.setAttribute('id', `consentno${nextChild}`)
    photoConsentNoInput.setAttribute('name', `childphotorelease${nextChild}`)
    photoConsentNoInput.setAttribute('value', '0')
    photoConsentNoInput.setAttribute('required', '')

    // Build form-check div
    photoConsentDiv.appendChild(photoConsentLabel)
    photoConsentYesDiv.appendChild(photoConsentYesInput)
    photoConsentYesDiv.appendChild(photoConsentYesLabel)
    photoConsentNoDiv.appendChild(photoConsentNoInput)
    photoConsentNoDiv.appendChild(photoConsentNoLabel)
    photoConsentDiv.appendChild(photoConsentYesDiv)
    photoConsentDiv.appendChild(photoConsentNoDiv)

    // Append form-group to form
    childrenDiv.appendChild(photoConsentDiv)

    // Create element for removing current child
    let removeChildButton = document.createElement('button')
    let removeChildButtonContent = document.createTextNode('Remove')
    removeChildButton.appendChild(removeChildButtonContent)

    // Set attributes for remove child button
    removeChildButton.setAttribute('type', 'button')
    removeChildButton.setAttribute('class', 'btn btn-secondary btn-sm')
    removeChildButton.setAttribute('id', `removeChild${nextChild}`)

    // Add event listener
    removeChildButton.addEventListener('click', () => {
      hr.remove()
      newChildDiv.remove()
      photoConsentDiv.remove()
      removeChildButton.remove()
    })

    // Append remove child button to form
    childrenDiv.appendChild(removeChildButton)

    // Incrememnt counter for next child
    nextChild++
  }
}

// Function to remove child
// function removeChild (event) {
//   const childId = event.target.getAttribute('id').substring(11)
//   const newChildDiv = document.getElementById(`newChild${childId}`)
//   const photoConsentDiv = document.getElementById(`photoConsent${childId}`)
//   childrenDiv.removeChild(newChildDiv)
//   childrenDiv.removeChild(photoConsentDiv)
//   childrenDiv.removeChild(event.target)
// }

// Get relevant DOM elements
const addChildButton = document.getElementById('addChild')
const childrenDiv = document.getElementById('children')

// Initialize child counter
let nextChild = 2

// Add event listeners to buttons
addChildButton.addEventListener('click', addChild)
