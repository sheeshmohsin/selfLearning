//checks if the browser supports WebRTC 

function hasUserMedia() { 
   navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia 
      || navigator.mozGetUserMedia || navigator.msGetUserMedia; 
   return !!navigator.getUserMedia; 
}
 
if (hasUserMedia()) { 
   navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia
      || navigator.mozGetUserMedia || navigator.msGetUserMedia;
		
   //get both video and audio streams from user's camera 
   navigator.getUserMedia({ video: true, audio: true }, function (stream) { 
      // console.log(stream);
      console.log(stream.getTracks());
      var video = document.querySelector('video'); 
		
      //insert stream into the video tag 
      video.src = window.URL.createObjectURL(stream); 
   }, function (err) {}); 
	
}else {
   alert("Error. WebRTC is not supported!"); 
}