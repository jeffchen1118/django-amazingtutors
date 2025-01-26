
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");



/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      e.preventDefault(); // Prevents the default behavior of the button
      let lessonSlug = e.target.getAttribute("lesson_slug");
      let answerId = e.target.getAttribute("answer_id");
      deleteConfirm.href = `/${lessonSlug}/answer_delete/${answerId}`;
      deleteModal.show();
    });
}