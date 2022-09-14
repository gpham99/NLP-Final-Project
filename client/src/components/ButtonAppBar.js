import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

const ButtonAppBar = () => {
    return (
    <Box sx={{ flexGrow: 1 }}>
        <AppBar position="absolute">
        <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Text Summarizer
        </Typography>
        </Toolbar>
    </AppBar>
    </Box>
);
}

export default ButtonAppBar;