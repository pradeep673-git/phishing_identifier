async function sendDetectionRequest(data) {
  const response = await fetch("http://localhost:8000/detect_phishing", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return response.json();
}

document.addEventListener('DOMContentLoaded', () => {
  // Example: Collect data from the current tab (replace with your logic)
  const detectionData = {
    url: "https://example.com",
    text: "Sample page text",
    audio_links: []
  };

  sendDetectionRequest(detectionData).then(result => {
    // Update your popup UI based on result
    document.getElementById('overall-status').textContent =
      result.overall === "safe" ? "🟢 Safe" :
      result.overall === "warning" ? "🟡 Suspicious" : "🔴 Dangerous";
    // ... update other fields similarly
  });
});
