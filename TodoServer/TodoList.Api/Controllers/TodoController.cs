using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace TodoList.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class TodoController : ControllerBase
{
    [Route("todos")]
    public IActionResult GetTodos()
    {
        try
        {
            List<Todo> todos = TaskQuery.GetTodos();
            List<TodoViewModel> todoViews = new List<TodoViewModel>();
            foreach (Todo todo in todos)
            {
                TodoViewModel todoViewModel = new TodoViewModel(todo.Id, todo.TaskName, TaskPropertiesConverter.ConvertPriorityToString(todo));
                todoViews.Add(todoViewModel);
            }

            return Ok(todoViews);
        }
        catch (Exception exception)
        {
            return Problem(exception.Message);
        }
    }

    [HttpPost]
    [Route("add")]
    public IActionResult InsertTodo([FromBody] Todo todo)
    {
        try
        {
            TaskQuery.SaveTodo(todo);
            return Ok("Task saved succesfully");
        }
        catch (Exception exception)
        {
            return Problem(exception.Message);
        }
    }

    [HttpPut]
    [Route("edit")]
    public IActionResult EditTodo([FromBody] Todo todo)
    {
        try
        {
            TaskQuery.EditTodo(todo);
            return Ok("Task edited successfully");
        }
        catch (Exception exception)
        {
            return Problem(exception.Message);
        }
    }

    [HttpDelete]
    [Route("delete")]
    public IActionResult DeleteTodo([FromBody] Todo todo)
    {
        try
        {
            TaskQuery.DeleteTodo(todo);
            return Ok("Task deleted successfully");
        }
        catch (Exception exception)
        {
            return Problem(exception.Message);
        }
    }
}
