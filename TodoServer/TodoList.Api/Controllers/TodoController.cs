using Api.Data.Models;
using Microsoft.AspNetCore.Mvc;
using TodoList.Api.ViewModels;
using TodoList.Data.Contracts;

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

    [HttpGet("{id}")]
    public async Task<ActionResult<Todo>> GetTodo([FromRoute] int id)
    {
        try
        {
            Todo todo = await _todoRepo.GetById(id.ToString());
            if (todo == null)
                return NotFound();

            return Ok(todo);
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
            await _todoRepo.Add(newTodo);
            
            return Ok(newTodo);
        }
        catch
        {
            return Problem();
        }
    }

    [HttpPost("markdone/{id}")]
    public async Task<ActionResult<Todo>> MarkTodoAsDone([FromRoute] int id)
    {
        try
        {
            Todo todo = await _todoRepo.GetById(id.ToString());

            if (todo.IsCompleted)
                todo.Uncomplete();
            else
                todo.MarkAsComplete();

            await _todoRepo.Update(todo);

            return Ok(todo);
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
            Todo todo = await _todoRepo.GetById(vm.Id.ToString());

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
            Todo todo = await _todoRepo.GetById(id.ToString());

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
