using Api.Data.Models;
using Dapper;
using Microsoft.Data.Sqlite;
using TodoList.Data.Contracts;
using TodoList.Data.SqliteConfiguration;

namespace TodoList.Data.Repositories;

public class SqliteTodoRepository : BaseSqlLiteRepository, IRepository<Todo>
{
    public SqliteTodoRepository(DatabaseConfig config) 
        : base(config)
    {
    }

    public async Task Add(Todo entity)
    {
        using SqliteConnection connection = GetConnection();

        string query = "INSERT INTO Todos (Id, Title, Description, CreatedAt, CompletedAt)" +
            " Values (@Id, @Title, @Description, @CreatedAt, @CompletedAt);";

        await connection.ExecuteAsync(query, entity);
    }

    public async Task Delete(Todo entity)
    {
        using SqliteConnection connection = GetConnection();

        string query = "DELETE FROM Todos Where Id = @Id";
        await connection.ExecuteAsync(query, new { entity.Id });
    }

    public async Task<Todo> GetById(string id)
    {
        using SqliteConnection connection = GetConnection();

        string query = "SELECT * FROM Todos WHERE Id = @Id;";
        return await connection.QueryFirstOrDefaultAsync<Todo>(query, new { Id = id });
    }

    public async Task<List<Todo>> GetAll()
    {
        using SqliteConnection connection = GetConnection();

        string query = "SELECT * FROM Todos;";
        var todos = await connection.QueryAsync<Todo>(query);
        return todos.ToList();
    }

    public async Task Update(Todo entity)
    {
        using SqliteConnection connection = GetConnection();

        string query = "UPDATE Todos SET Title = @Title, Description = @Description, " +
            "CreatedAt = @CreatedAt, CompletedAt = @CompletedAt Where Id = @Id";
        await connection.ExecuteAsync(query, entity);
    }
}
