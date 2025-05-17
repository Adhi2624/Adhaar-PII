import React, { useState } from 'react';
import axios from 'axios';
import './App.css'
import { use } from 'react';
function App() {
  const [fileData, setFileData] = useState({ file: null, type: '' });
  const [parsedOutput, setParsedOutput] = useState(null);
  const [parsedText , setParsedText]=useState("");
  const [uploading, setUploading] = useState(false);
  const [retrivedImage, setRetrivedImage]=useState("")
  const acceptedFileTypes = ["application/pdf", "image/jpeg", "image/jpg"];

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;

    let fileType = selectedFile.type;
    if (acceptedFileTypes.includes(fileType)) {
      setFileData({
        file: selectedFile,
        type: fileType
      });
    } else {
      alert("Please upload a valid file type (PDF, JPEG, JPG)");
      e.target.value = null;
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!fileData.file) {
      alert('Please upload a file first.');
      return;
    }

    const formdata = new FormData();
    formdata.append('file', fileData.file);
    formdata.append('type', fileData.type);

    try {
      setUploading(true)
      const res = await axios.post('http://localhost:8000/upload', formdata, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      let raw = res.data;
      const rawValue = Object.values(raw)[0]; 
      console.log(res.data[1])
      const parsedJson = JSON.parse(rawValue); 
      setParsedOutput(parsedJson);
      setParsedText(res.data[1])
      setRetrivedImage(res.data[2])
    } catch (err) {
      console.error('Upload failed:', err);
      alert('Something went wrong. Try again.');
    }
    setUploading(false)
  };

  return (
    <>
      <h1>Adhaar Data PII Masking Application</h1>

      <form onSubmit={handleSubmit}>
        <label>
          Upload your Aadhaar file (Image or PDF):
          
        </label>
        <input
            type="file"
            name="file"
            accept="application/pdf,image/jpeg,image/jpg"
            onChange={handleFileChange}
          />
        <button type="submit">Upload</button>
      </form>
    {uploading && (<h3>Please wait the file is  processing.....</h3>)}
      {parsedOutput && (
  <div style={{ marginTop: '20px' }} className='outputtable'>
    <table border="1" cellPadding="10">
      <tbody>
        {Object.entries(parsedOutput).map(([key, value]) => (
          <tr key={key}>
            <td>{key}</td>
            <td>{value}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
)}

{
  retrivedImage && (
    <img src={retrivedImage} alt="retrived image" />
  )
}

{parsedText &&(
  <div className='parsedText'>
    <h2>Parsed Text</h2>
    <pre>{parsedText}</pre>
  </div>
) 

}


    </>
  );
}

export default App;
