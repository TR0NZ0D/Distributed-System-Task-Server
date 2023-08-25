using Api.Data.Models;
using TodoList.Data.Contracts;
using TodoList.Data.Repositories;
using TodoList.Data.SqliteConfiguration;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Repositories
DatabaseConfig dbConfig = new() { Name = builder.Configuration["DatabaseName"] };
DatabaseBootstrap bootstrap = new DatabaseBootstrap(dbConfig);
bootstrap.Setup();

builder.Services.AddSingleton(dbConfig);

builder.Services.AddSingleton<IRepository<Todo>, SqliteTodoRepository>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
