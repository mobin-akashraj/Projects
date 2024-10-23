// Function to generate a random password
function generatePassword() {
    const length = document.getElementById('lengthSlider').value; // Get the length from the slider
    const includeLowercase = document.getElementById('lowercase').checked;
    const includeUppercase = document.getElementById('uppercase').checked;
    const includeNumbers = document.getElementById('numbers').checked;
    const includeSymbols = document.getElementById('symbols').checked;

    const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numberChars = '0123456789';
    const symbolChars = '!@#$%^&*()_+[]{}|;:,.<>?';

    let validChars = '';
    if (includeLowercase) validChars += lowercaseChars;
    if (includeUppercase) validChars += uppercaseChars;
    if (includeNumbers) validChars += numberChars;
    if (includeSymbols) validChars += symbolChars;

    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * validChars.length);
        password += validChars[randomIndex];
    }

    const passwordInput = document.getElementById('password');
    passwordInput.value = password; // Set the generated password in the input field
}

// Function to update the displayed length value
function updateLengthValue() {
    const lengthSlider = document.getElementById('lengthSlider');
    const lengthValue = document.getElementById('lengthValue');
    lengthValue.textContent = lengthSlider.value; // Update the displayed value
}

// Function to copy the password to clipboard
function copyPassword() {
    const passwordInput = document.getElementById('password');
    passwordInput.select();
    document.execCommand('copy'); // Copy the password
}
