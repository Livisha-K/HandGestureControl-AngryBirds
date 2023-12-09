<!DOCTYPE html>
<html>
<body>

  <h1>Hand Gesture Control for Angry Birds</h1>

  <p>This Python script transforms hand gestures into controls for Angry Birds using OpenCV, MediaPipe, and PyAutoGUI. The program captures video from the default camera, tracks hand movements, and translates specific gestures into mouse actions for an interactive gaming experience.</p>

  <h2>Requirements</h2>
  <ul>
      <li>Python</li>
      <li>OpenCV</li>
      <li>MediaPipe</li>
      <li>PyAutoGUI</li>
  </ul>

  <h2>Code Overview</h2>
  <p>The script comprises the following main features:</p>

  <ol>
      <li>Import necessary libraries: OpenCV, MediaPipe, PyAutoGUI, and Math.</li>
      <li>Disable PyAutoGUI fail-safe to prevent unexpected program exits.</li>
      <li>Initialize video capture from the default camera and create MediaPipe Hands instance.</li>
      <li>Define functions to move the cursor, change directions, get current hand position, and detect pinch gestures.</li>
      <li>Inside the main loop:
          <ul>
              <li>Read frames from the camera and process them to detect hand landmarks.</li>
              <li>Draw hand landmarks on the video feed.</li>
              <li>Perform actions based on pinch gestures:
                  <ul>
                      <li>Mouse click when a pinch is detected.</li>
                      <li>Update cursor direction and position.</li>
                  </ul>
              </li>
              <li>Release the mouse click when the pinch is released.</li>
              <li>Show the processed video feed with hand landmarks.</li>
              <li>Exit the loop if the 'q' key is pressed.</li>
          </ul>
      </li>
  </ol>

  <h2>Usage</h2>
  <p>Ensure that the required libraries are installed before running the script. The program allows you to control Angry Birds using your hand gestures captured by the camera.</p>

  <h2>Important Notes</h2>
  <ul>
      <li>This script assumes that Angry Birds is running and active.</li>
      <li>Adjustments may be necessary for optimal hand gesture detection based on environmental conditions and camera placement.</li>
      <li>Exit the program by pressing the 'q' key in the output window.</li>
  </ul>

  <h2>Author</h2>
  <p>Author: Livisha K</p>

</body>

</html>
