import * as React from 'react';

const UploadButton = () => {
    return (
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept="application/pdf" />
            <input type="submit" />
        </form>
    );
}

export default UploadButton;