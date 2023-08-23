namespace TodoList.Api.Contracts;

public interface IRepository<T> where T : class
{
    Task<List<T>> GetAll();
    Task<T> Add(T entity);
    Task<T> Update(T entity);
    Task<T> Delete(T entity);
}
