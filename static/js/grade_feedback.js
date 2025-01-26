function clearContent() {
    const gradeInput = document.getElementById('id_grade');
    const feedbackInput = document.getElementById('id_feedback');
    
    if (gradeInput) {
        gradeInput.value = 0.0;
    }
    
    if (feedbackInput) {
        feedbackInput.value = '';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button.btn-primary[type="button"]').addEventListener('click', clearContent);
});
