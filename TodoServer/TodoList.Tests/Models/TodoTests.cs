using Api.Data.Models;

namespace TodoList.Tests.Models;

public class TodoTests
{
    [Test]
    public void MarkAsComplete_WhenCalled_SetADateTime()
    {
        Todo todo = new("Clean the house");
        Assert.IsNull(todo.CompletedAt);

        todo.MarkAsComplete();
        Assert.IsNotNull(todo.CompletedAt);
    }

    [Test]
    public void MarkAsComplete_WhenCalled_SetIsCompletedCorrectly()
    {
        Todo todo = new("Clean the house");
        Assert.IsFalse(todo.IsCompleted);

        todo.MarkAsComplete();
        Assert.IsTrue(todo.IsCompleted);
    }

    [Test]
    public void Uncomplete_WhenCalled_SetPropertiesCorrectly()
    {
        Todo todo = new("Clean the house");
        todo.MarkAsComplete();

        todo.Uncomplete();
        Assert.IsFalse(todo.IsCompleted);
        Assert.IsNull(todo.CompletedAt);
    }
}
