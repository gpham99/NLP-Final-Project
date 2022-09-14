import * as React from 'react';

const UploadButton = () => {
    return (
        <form >
            <input id="contained-button-file" type="file" accept="application/pdf" />
            <input type="submit" />
        </form>
    );
}

export default UploadButton;