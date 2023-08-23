using Api.Data.Models;
using Microsoft.AspNetCore.Mvc;
using TodoList.Api.Contracts;
using TodoList.Api.ViewModels;

namespace TodoList.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class TodoController : ControllerBase
{
    private readonly IRepository<Todo> _todoRepo;

    public TodoController(IRepository<Todo> todoRepo)
    {
        _todoRepo = todoRepo;
    }

    [HttpGet]
    public async Task<ActionResult<List<Todo>>> GetTodos()
    {
        try
        {
            List<Todo> todos = await _todoRepo.GetAll();
            return Ok(todos);
        }
        catch
        {
            return Problem();
        }
    }

    [HttpPost]
    public async Task<ActionResult<Todo>> AddTodo([FromBody] NewTodoViewModel todo)
    {
        try
        {
            Todo newTodo = new(todo.title, todo.description);
            Todo todoInserted = await _todoRepo.Add(newTodo);

            return Ok(todoInserted);
        }
        catch
        {
            return Problem();
        }
    }

    [HttpPut]
    public async Task<ActionResult<Todo>> EditTodo([FromBody] UpdateTodoViewModel vm)
    {
        try
        {
            Todo todo = await _todoRepo.Get(x => x.Id == vm.Id);

            if (todo == null)
                return NotFound();

            todo.Update(vm.Title, vm.Description);

            await _todoRepo.Update(todo);
            return StatusCode(StatusCodes.Status201Created, todo);
        }
        catch
        {
            return Problem();
        }
    }

    [HttpDelete]
    [Route("{id}")]
    public async Task<ActionResult> DeleteTodo([FromRoute] int id)
    {
        try
        {
            Todo todo = await _todoRepo.Get(x => x.Id == id);

            if (todo == null)
                return NotFound();

            return Ok();
        }
        catch
        {
            return Problem();
        }
    }
}
