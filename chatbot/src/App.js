import './App.css';
import chatBot from './components/chatBot';
import Button from '@mui/material/Button';
import ArrowRightIcon from '@mui/icons-material/ArrowRight';
import { useState } from 'react';
import axios from 'axios';
// import SearchIcon from '@mui/icons-material/Search';

function App() {

  const [request,setRequest]=useState("");
  const [responseData,setResponseData]=useState("");
  const [showResponse,setShowResponse]=useState(false);

  const onResponseSubmit=async()=>{
    console.log("Hello");
    const {data}=await axios.post('http://localhost:5000/',{
        request:request
        }, {     
        headers:{
            'Content-Type':'multipart/form-data'
        }
    })
    setResponseData(data.substr(2,data.length-4));
    setShowResponse(true);
    console.log(`Data ${data}`)

  }

  const handleChange=(event)=>{
    setRequest(event.target.value);
    console.log(request);
  }


  return (
    <div className="App">
      <div className='header'>FinBot</div>
      <div className='response'>
        {
          showResponse ? 
          <div className='response-text'>
          {responseData}
          </div>
          :
          <div></div>
        }
      </div>
      <div className='input-container'>
        <input className='input-box' placeholder='How may I help you?' onChange={handleChange} type='text'/>
        <Button variant="text" onClick={onResponseSubmit}><ArrowRightIcon fontSize='large'/></Button>
      </div>
    </div>
  );
}

export default App;
