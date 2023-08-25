using Microsoft.Data.Sqlite;
using TodoList.Data.SqliteConfiguration;

namespace TodoList.Data.Repositories;

public abstract class BaseSqlLiteRepository
{
    private readonly DatabaseConfig _config;

    protected BaseSqlLiteRepository(DatabaseConfig config)
    {
        _config = config;
    }

    protected SqliteConnection GetConnection()
    {
        return new SqliteConnection(_config.Name);
    }
}
