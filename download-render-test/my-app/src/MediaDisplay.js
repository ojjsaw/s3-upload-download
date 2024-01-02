import React from 'react';

function MediaDisplay({ imageUrl, textFileUrl, videoUrl, audioUrl }) {
  const [text, setText] = React.useState('');

  React.useEffect(() => {
    fetch(textFileUrl)
      .then(response => response.text())
      .then(data => setText(data))
      .catch(error => console.error('Error fetching text file:', error));
  }, [textFileUrl]);

  return (
    <div>
      <h1>Image Display</h1>
      {imageUrl && <img src={imageUrl} width="50%" alt="From S3" />}
      <h1>Text Display</h1>
      {text && (
        <div>
          <textarea value={text} readOnly style={{ width: '50%', height: '200px' }} />
        </div>
      )}
      <h1>Video Display</h1>
      {videoUrl && <video src={videoUrl} width="50%" controls />}
      <h1>Audio Display</h1>
      {audioUrl && <audio src={audioUrl} width="50%" controls />}
    </div>
  );
}

export default MediaDisplay;
