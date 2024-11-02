function openYouTube() {
    window.open("https://www.youtube.com/channel/UC-0mjbkLt6kqndzCb3Go-Ww", "_blank");
  }
  
  function startPouring() {
    // Hide reverse GIF and show pouring GIF
    document.getElementById("reverseGif").style.opacity = 0;
    const pouringGif = document.getElementById("pouringGif");
    pouringGif.style.opacity = 1;
  
    // Reset GIF by reloading src to play it from the start
    pouringGif.src = "";
    pouringGif.src = "change2.gif";
  }
  
  function startReversing() {
    // Hide pouring GIF and show reverse GIF
    document.getElementById("pouringGif").style.opacity = 0;
    const reverseGif = document.getElementById("reverseGif");
    reverseGif.style.opacity = 1;
  
    // Reset reverse GIF and play it
    reverseGif.src = "";
    reverseGif.src = "change2-reverse.gif";
  
    // Hide the reverse GIF after it completes (assuming it's 1.2 seconds long)
    setTimeout(() => {
      reverseGif.style.opacity = 0;
    }, 1200); // Adjust time to match the duration of change2-reverse.gif
  }