using Dapper;
using Microsoft.Data.Sqlite;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TodoList.Data.SqliteConfiguration;
public class DatabaseBootstrap
{
    private readonly DatabaseConfig _dbConfig;

    public DatabaseBootstrap(DatabaseConfig dbConfig)
    {
        _dbConfig = dbConfig;
    }

    public void Setup()
    {
        using SqliteConnection connection = new(_dbConfig.Name);

        var table = connection.Query<string>("SELECT name FROM sqlite_master WHERE type='table' AND name = 'Todos';");
        var tableName = table.FirstOrDefault();

        if (!string.IsNullOrEmpty(tableName))
            return;

        connection.Execute("Create Table Todos (" +
            "Id INTEGER PRIMARY KEY AUTOINCREMENT, " +
            "Title VARCHAR(100) NOT NULL, " +
            "Description VARCHAR(500), " +
            "CreatedAt DATE NOT NULL, " +
            "CompletedAt DATE)");
    }
}
