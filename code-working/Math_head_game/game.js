// Constants and global variables
const options = ['+', '-'];
let correctAnswer;
let currentEquation = {};
let optionSelected = false;  // Prevent multiple detections for the same equation

// Start the camera and load the game
async function startGame() {
    try {
        // Access the user's camera
        const video = document.getElementById('camera');
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;

        console.log("Camera started successfully");
        
        generateEquation();
        detectHeadPosition(video);
    } catch (error) {
        console.error("Error accessing camera: ", error);
    }
}

// Generate a simple math equation with missing operation
function generateEquation() {
    const num1 = Math.floor(Math.random() * 10);
    const num2 = Math.floor(Math.random() * 10);
    
    // Randomly choose an operation for the correct answer
    const correctOperation = options[Math.floor(Math.random() * options.length)];
    correctAnswer = eval(`${num1} ${correctOperation} ${num2}`);
    
    // Save the current equation state for reference
    currentEquation = { num1, num2, correctOperation };
    
    // Display the equation with a blank for the operation
    document.getElementById('equationText').textContent = `${num1} _ ${num2} = ${correctAnswer}`;
    optionSelected = false;  // Reset option selected for new equation

    console.log("Equation generated:", `${num1} _ ${num2} = ${correctAnswer}`);
}

// Detect head position and determine if it’s in left or right zone
async function detectHeadPosition(video) {
    try {
        const model = await faceLandmarksDetection.load(faceLandmarksDetection.SupportedPackages.mediapipeFacemesh);
        console.log("Face landmarks detection model loaded successfully");

        const detectFace = async () => {
            const predictions = await model.estimateFaces({ input: video });

            if (predictions.length > 0 && !optionSelected) {  // Only proceed if no option has been selected
                const headX = predictions[0].boundingBox.topLeft[0];
                const screenWidth = video.videoWidth;

                console.log("Head X position:", headX, "Screen width:", screenWidth);

                // Define left and right zones based on screen width
                const leftZone = screenWidth / 3;       // Left third of screen for "+"
                const rightZone = (2 * screenWidth) / 3; // Right third of screen for "-"

                // Check if head is within the left or right zone
                if (headX < leftZone) {
                    console.log("Head in left zone, selecting +");
                    selectOption('+');  // Head in left zone selects "+"
                } else if (headX > rightZone) {
                    console.log("Head in right zone, selecting -");
                    selectOption('-');  // Head in right zone selects "-"
                }
            }

            requestAnimationFrame(detectFace);  // Continue detecting in a loop
        };

        detectFace();
    } catch (error) {
        console.error("Error in face detection:", error);
    }
}

// Handle option selection based on head position
function selectOption(selectedOption) {
    // Update the displayed equation with the selected operation
    document.getElementById('equationText').textContent = 
        `${currentEquation.num1} ${selectedOption} ${currentEquation.num2} = ${correctAnswer}`;
    
    // Check if the chosen operation is correct
    const isCorrect = selectedOption === currentEquation.correctOperation;

    optionSelected = true;  // Mark the option as selected to avoid multiple triggers

    if (isCorrect) {
        alert("Correct! Starting new equation...");
        generateEquation();
    } else {
        alert("Incorrect! Game over.");
        location.reload();
    }
}

// Start the game
startGame();
