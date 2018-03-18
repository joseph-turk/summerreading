// Function to add new child name input
function addChild () {
  let lastChild = document.getElementById(`childname${nextChild - 1}`)
  if (lastChild.value === '') {
    // Prevent adding another child if blank input is available
    lastChild.focus()
  } else {
    // Create elements for form group
    let newChildDiv = document.createElement('div')
    let newChildLabel = document.createElement('label')
    let labelContent = document.createTextNode('Child\'s Name')
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
    
    // Incrememnt counter for next child
    nextChild++
  }  
}

// Get relevant DOM elements
const addChildButton = document.getElementById('addChild')
const childrenDiv = document.getElementById('children')

// Initialize child counter
let nextChild = 2

// Add event listeners to buttons
addChildButton.addEventListener('click', addChild)
