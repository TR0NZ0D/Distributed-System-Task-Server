using System.ComponentModel.DataAnnotations;

namespace TodoList.Api.ViewModels;

public record UpdateTodoViewModel(
    [Required(ErrorMessage = "Id is required")] int Id, 
    [Required(AllowEmptyStrings = false, ErrorMessage = "Title is required")] string Title,
    string Description
    );
