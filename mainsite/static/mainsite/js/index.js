$(document).ready(function() {
    $("form").submit(onSubmit)
    $(".delete_action").click(onDeleteClick)
})


function onSubmit() {
    console.log("onSubmit reached")
    event.preventDefault()
    data = {
             'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
             'course_name':         $("#course_name").val(),
             'course_description':  $("#course_description").val()
           }
    
    response = $.post('api/courses/new', data).done(function(response) {
        console.log(response)
        if(response.success) {
            console.log("success!")
            $("tbody").append(
                               "<tr>" +
                                   "<td class=\"table_name\">" +
                                       response.course.name +
                                   "</td>" +
                                   "<td class=\"table_description\">" +
                                       response.course.description +
                                   "</td>" +
                                   "<td class=\"table_date_added\">" +
                                       response.course.created_at +
                                   "</td>" +
                                   "<td class=\"table_links\">" +
                                       "<a href=\"/courses/" + response.course.id + "\">" +
                                           "Read Comments" +
                                       "</a>" +
                                   "</td>" +
                                   "<td class=\"table_actions\">" +
                                       "<a href=\"/courses/" + response.course.id + "/confirm_delete\" class=\"delete_action\">" +
                                           "Remove Course" +
                                       "</a>" +
                                   "</td>" +
                               "</tr>"
                             )
            // Reapply events to ensure new link has event attached
            $(".delete_action").click(onDeleteClick)
        }
    })
}


function onDeleteClick() {
    event.preventDefault()
    console.log("Delete anchor clicked!")
}
