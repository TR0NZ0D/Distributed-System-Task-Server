using System.ComponentModel.DataAnnotations;

namespace TodoList.Api.ViewModels;

public record NewTodoViewModel([Required(AllowEmptyStrings = false, ErrorMessage = "Title is required")] string? title, string? description);
