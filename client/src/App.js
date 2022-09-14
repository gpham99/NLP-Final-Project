import React, {useState, useEffect} from 'react';
import ButtonAppBar from './components/ButtonAppBar';
import UploadButton from './components/UploadButton';
import Grid from '@mui/material/Grid';

function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    // app bar
    
    // button to upload -> validation (must be PDF file) -- once verified it's PDF
    
    // a bunch of buttons to choose how specific the result should be (button group)

    // text box to return the answer

    <Grid container direction="column" spacing={15} alignItems="center">
      <Grid item>
        <ButtonAppBar></ButtonAppBar>    
      </Grid>

      <Grid item>
        <UploadButton></UploadButton>
      </Grid>
    </Grid>
  );
}

export default App;
