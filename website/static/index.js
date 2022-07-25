function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}


function uploadFile() {
    cropperInstance.getCroppedCanvas().toBlob(function(blob) {
        const formData = new FormData();
        formData.append('avatar', blob);
        fetch('xxxx', {
            method: 'POST',
            body: formData
        });
    });
}