document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.student-btn').addEventListener('click', showStudentForm);
    document.querySelector('.tutor-btn').addEventListener('click', showTutorForm);
});

function showStudentForm() {
    document.getElementById('student-form').style.display = 'block';
    document.getElementById('tutor-form').style.display = 'none';
}

function showTutorForm() {
    document.getElementById('student-form').style.display = 'none';
    document.getElementById('tutor-form').style.display = 'block';
}
