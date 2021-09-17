$(document).ready(function() {
    $("form").submit(onSubmit)
    $(".delete_action").click(onDeleteClick)

    $("#modal_yes").click(onDelete)
    $("#modal_no").click(function() { $("#modal_popup").hide() })
})


function onSubmit() {
    event.preventDefault()
    data = {
             'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
             'course_name':         $("#course_name").val(),
             'course_description':  $("#course_description").val()
           }
    
    response = $.post('api/courses/new', data).done(function(response) {
        if(response.success) {
            $("tbody").append(
                               "<tr id=\"course" + response.course.id + "\">" +
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
                                       "<a href=\"courses/" + response.course.id + "/confirm_delete\" class=\"delete_action\">" +
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
    // Get course name
    anchor = $(this).attr('href')
    curr_course_id = anchor.substring(anchor.indexOf('/')+1, anchor.lastIndexOf('/'))
    response = $.ajax('/api/courses/' + curr_course_id + "/get").done(function(response) {
        if(response.success) {
                curr_course_name = response.course.name
            }

            // Populate modal before showing it
            $("#modal_course_id").text(curr_course_id)
            $(".modal_course_name").text(curr_course_name)
            $("#modal_popup").show()
            $("#modal_course_id").hide()
    })
}


function onDelete() {
    $("#modal_popup").hide()
    curr_course_id = $("#modal_course_id").text()
    response = $.ajax('/api/courses/' + curr_course_id + '/delete').done(function(response) {
        if(response.success) {
            $("#course" + curr_course_id).remove()
        }

    })
}
