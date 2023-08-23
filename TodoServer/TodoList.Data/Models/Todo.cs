using System.Text.Json.Serialization;

namespace Api.Data.Models
{
    public class Todo
    {
        public int Id { get; set; }

        private string? _title;
        public string? Title 
        {
            get { return _title; }
            set
            {
                if (string.IsNullOrEmpty(value))
                    throw new ArgumentNullException("Invalid title");

                _title = value;
            }
        }
        public string? Description { get; set; }
        public DateTime? CreatedAt { get; private set; }
        public DateTime? CompletedAt { get; private set; }

        public bool IsCompleted => CompletedAt != null;

        public Todo(string title)
        {
            Title = title;
            CreatedAt = DateTime.Now;
        }

        public Todo(string? title, string? description)
        {
            Title = title;
            Description = description;
            CreatedAt = DateTime.Now;
        }

        public Todo(int id, string? title, string? description, DateTime createdAt, DateTime? completedAt) 
            : this(title, description)
        {
            Id = id;
            CreatedAt = createdAt;
            CompletedAt = completedAt;
        }

        public void MarkAsComplete()
        {
            CompletedAt = DateTime.Now;
        }

        public void Uncomplete()
        {
            CompletedAt = null;
        }
    }
}
