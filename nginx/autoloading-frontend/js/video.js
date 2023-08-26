navigator.mediaDevices.getUserMedia({ video: true }) // 获取视频流
  .then(function(stream) {
    var video = document.getElementById('videoElement');
    video.srcObject = stream;
  })
  .catch(function(error) {
    console.log("无法获取视频流: " + error);
  });