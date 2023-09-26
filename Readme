## Standard Project Structure for Monolithic Architecture with .NET Core 6.0

### Project Structure
```
├── README.md
├── .gitignore
├── .gitattributes
├── src
│   ├── Logs
│   │   ├── Log1.txt
│   │   ├── Log2.txt
│   │   ├── ....
│   ├── wwwroot
│   │   ├── uploads
│   │   ├── ....
│   ├── Controller
│   │   └── Controller.cs
│   ├── Data
│   │   ├── Context1
│   │   │   ├── DbContext1.cs
│   │   │   ├── Migrations
│   │   ├── Context2
│   │   │   ├── DbContext2.cs
│   │   │   ├── Migrations
│   │   ├── ....
│   ├── Models
│   │   └── Entities 
│   │   │   ├── Entities of Context1
│   │   │   ├── Entities of Context2
│   │   │   ├── ....
│   │   │── RequestModels
│   │   │   ├── RequestModel1.cs
│   │   │   ├── RequestModel2.cs
│   │   │   ├── ....
│   │   │── ResponseModels
│   │   │   ├── ResponseModel1.cs
│   │   │   ├── ResponseModel2.cs
│   │   │   ├── ....
│   ├── Services (Business Logic)
│   │   ├── Service1.cs
│   │   ├── Service2.cs
│   │   ├── ....
│   ├── Utils
│   │   ├── TokenHelper.cs
|   |   ├── CryptoHelper.cs
│   │   ├── ....
|   ├── Middleware
|   |   |   ├── ExceptionMiddleware.cs
|   |   |   ├── ....
│   ├── appsettings.json
│   ├── Program.cs
├── Test
│   ├── Controller
│   │   └── ControllerTest.cs
│   ├── Services
│   │   └── ServiceTest.cs
│   ├── Utils
│   │   └── UtilsTest.cs
│   ├── appsettings.json
│   ├── Program.cs
├── ProjectName.sln
```
### Eplain Project Structure
- **Controller**: Controller of project
- **Data**: Data Access Layer
- **Models**: Models of project
- **Services**: Business Logic Layer 
- **Utils**: Utilities of project
- **Middleware**: Middleware of project
- **Program.cs**: Main class of project

# How to use

## Git Convention
### 1. Create a new Repository
- Create a new repository with name is **ProjectName**
- Then make sure you have a **.gitignore** file in your repository, You can clone **StandardProjectStructure** repository and copy **.gitignore** file to your repository
- The reason why you need to have a **.gitignore** file in your repository is because you don't want to push unnecessary files to your repository, it will make your repository bigger and bigger and it will take a lot of time to clone your repository to your local machine or your server, when you use Cloud Server like AWS, Azure, Google Cloud, ... it will take a lot of money to store your repository


## Coding Convention
### 1. Create a new project
- Create a new project with name is **ProjectName**
- Create a new folder with name is **ProjectName**
- Copy all files in **StandardProjectStructure** folder to **ProjectName** folder

### 2. Setup project
- Open **ProjectName.sln** file with Visual Studio 
- Change **ProjectName** in **ProjectName.sln** file to your project name

### 3. Setup Database
- Open **Package Manager Console** in Visual Studio and install all packages nessesary for project
- Example:
```bash
Install-Package Microsoft.EntityFrameworkCore.SqlServer
Install-Package Microsoft.EntityFrameworkCore.Tools
Install-Package Microsoft.EntityFrameworkCore.Design
...
```
- Next step, need to config connection string to connect to database in **appsettings.json** file or **appsettings.Development.json** file it depend on your environment
- Example:
```json
"ConnectionStrings": {
	"DefaultConnection": "Server=.;Database=ProjectName;Trusted_Connection=True;MultipleActiveResultSets=true",
	"Connection1": "Server=.;Database=ProjectName1;Trusted_Connection=True;MultipleActiveResultSets=true",
	"Connection2": "Server=.;Database=ProjectName2;Trusted_Connection=True;MultipleActiveResultSets=true"
  }
```
### 3.1 Setup Database with code first
####  3.1.1: 
- First, You need create Entity class in **Model** folder
- Example:
```csharp
public class Table1
{
	public int Id { get; set; }
	public string Name { get; set; }
	public string Description { get; set; }
}
```
#### 3.1.2:
- Next, Need to create a new class in **Data** folder with name is **ProjectNameDbContext.cs**
- Example:
```csharp
public class ProjectNameDbContext : DbContext
{
	public ProjectNameDbContext(DbContextOptions<ProjectNameDbContext> options) : base(options)
	{
	}

	protected override void OnModelCreating(ModelBuilder modelBuilder)
	{
		base.OnModelCreating(modelBuilder);
	}

	public DbSet<Table1> Table1 { get; set; }
	public DbSet<Table2> Table2 { get; set; }
	public DbSet<Table3> Table3 { get; set; }
	...

	//if it have a relationship, you need to config it
	protected override void OnModelCreating(ModelBuilder modelBuilder)
	{
		base.OnModelCreating(modelBuilder);
		modelBuilder.Entity<Table1>().HasMany(x => x.Table2).WithOne(x => x.Table1).HasForeignKey(x => x.Table1Id);
		modelBuilder.Entity<Table2>().HasMany(x => x.Table3).WithOne(x => x.Table2).HasForeignKey(x => x.Table2Id);
		...
	}
}
```
- It will same with other DbContext class

#### 3.1.3:
- After that, Need to migrate database with command in **Package Manager Console**
```bash
Add-Migration InitialCreate -Context ProjectNameDbContext -OutputDir Data/Context1/Migrations
```
- In teminal command:
```bash
dotnet ef migrations add InitialCreate --context ProjectNameDbContext --output-dir Data/Context1/Migrations
```

- Next, Update database with command in **Package Manager Console**
```bash
Update-Database -Context ProjectNameDbContext
```
- In teminal command:
```bash
dotnet ef database update --context ProjectNameDbContext
```

### 3.2 Setup Database with database first
#### 3.2.1:
- First, Design database with any engine database require (SQL Server, MySQL, PostgreSQL, ...)
- But you have to config connection string to connect to database in **appsettings.json** file or **appsettings.Development.json** file it depend on your environment
#### 3.2.2:
- Then you can use **Scaffold-DbContext** command in **Package Manager Console** to generate DbContext class and Entity class
```bash
Scaffold-DbContext "Name=ConnectionStrings:Connection1" Microsoft.EntityFrameworkCore.SqlServer -ContextDir Data/Context1 -Context ProjectNameDbContext -OutputDir Models/Entities/Context1
```
```bash

Scaffold-DbContext "Name=ConnectionStrings:Connection2" Microsoft.EntityFrameworkCore.SqlServer -ContextDir Data/Context2 -Context ProjectNameDbContext -OutputDir Models/Entities/Context2
```
- In teminal command:
```bash
dotnet ef dbcontext scaffold "Name=ConnectionStrings:Connection1" Microsoft.EntityFrameworkCore.SqlServer -o Data/Context1 -c ProjectNameDbContext

dotnet ef dbcontext scaffold "Name=ConnectionStrings:Connection2" Microsoft.EntityFrameworkCore.SqlServer -o Data/Context2 -c ProjectNameDbContext
```
- If you use MySQL, PostgreSQL, ... you need to change **Microsoft.EntityFrameworkCore.SqlServer** to **Pomelo.EntityFrameworkCore.MySql**, **Npgsql.EntityFrameworkCore.PostgreSQL**, ...

### 4. Setup Authentication
#### 4.1 Setup Authentication with JWT
- You should use **JWT** for authentication or **Identity** for authentication
- If you use **JWT** for authentication, you need to config **JWT** in **appsettings.json** file or **appsettings.Development.json** file it depend on your environment
- Example:
```json
"JWT": {
	"Key": "This is key for JWT",
	"Issuer": "This is issuer for JWT",
	"Audience": "This is audience for JWT",
	"AccessTokenExpiration": 60,
	"RefreshTokenExpiration": 60
  }
```
- Next, you need to config **JWT** in **Program.cs** file
- Example:
```csharp
services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
	.AddJwtBearer(options =>
	{
		options.TokenValidationParameters = new TokenValidationParameters
		{
			ValidateIssuer = true,
			ValidateAudience = true,
			ValidateLifetime = true,
			ValidateIssuerSigningKey = true,
			ValidIssuer = Configuration["JWT:Issuer"],
			ValidAudience = Configuration["JWT:Audience"],
			IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(Configuration["JWT:Key"]))
		};
	});
```

- Then you can use **Authorize** attribute for authorization
- Example:
```csharp
[Authorize]
[HttpGet]
public IActionResult Get()
{
	return Ok();
}
```
and you can use **AllowAnonymous** attribute for authorization
- Example:
```csharp
[AllowAnonymous]
[HttpPost]
public IActionResult Login()
{
	return Ok();
}
```
- When you want to get token, you can use **TokenHelper** class in **Utils** folder
- Example:
```csharp
var token = TokenHelper.GenerateToken(user, _configuration);

public static class TokenHelper
{
	public static string GenerateToken(User user, IConfiguration configuration)
	{
		var tokenHandler = new JwtSecurityTokenHandler();
		var key = Encoding.ASCII.GetBytes(configuration["JWT:Key"]);
		var tokenDescriptor = new SecurityTokenDescriptor
		{
			Subject = new ClaimsIdentity(new Claim[]
			{
				new Claim(ClaimTypes.Name, user.Id.ToString()),
				new Claim(ClaimTypes.Role, user.Role.ToString())
			}),
			Expires = DateTime.UtcNow.AddMinutes(Convert.ToInt32(configuration["JWT:AccessTokenExpiration"])),
			SigningCredentials = new SigningCredentials(new SymmetricSecurityKey(key), SecurityAlgorithms.HmacSha256Signature)
		};
		var token = tokenHandler.CreateToken(tokenDescriptor);
		return tokenHandler.WriteToken(token);
	}
}

```
- Then you want to get user information from token, you can use **HttpContext** class
- Example:
```csharp
	var userId = HttpContext.User.Claims.FirstOrDefault(x => x.Type == ClaimTypes.Name).Value;
```
- If it have a role, you can use **Authorize** attribute with role
- Example:
```csharp
[Authorize(Roles = "Admin")]
[HttpGet]
public IActionResult Get()
{
	return Ok();
}
```

### 5. Setup the routing
- You can use **Route** attribute for routing
- Example:
```csharp
[Route("api/[controller]")]
[ApiController]
public class Controller : ControllerBase
{
	[HttpGet]
	public IActionResult Get()
	{
		return Ok();
	}
}
// Result: api/Controller
```
- Or you can use only an attribute for a controller
- Example:
```csharp
[ApiController]
[Route("api/[controller]/[action]")]
public class Controller : ControllerBase
{
	[HttpGet]
	public IActionResult Get()
	{
		return Ok();
	}
}
// Result: api/Controller/Get
```
- Or you can use in a method
- Example:
```csharp
[ApiController]
[Route("api/[controller]")]
public class Controller : ControllerBase
{
	[HttpGet("Get")]
	public IActionResult Get()
	{
		return Ok();
	}
}
// Result: api/Controller/Get
```

### 6. Setup the middleware
- You can use **Middleware** for handle request
- Example:
```csharp
public class ExceptionMiddleware
{
	private readonly RequestDelegate _next;
	private readonly ILogger<ExceptionMiddleware> _logger;

	public ExceptionMiddleware(RequestDelegate next, ILogger<ExceptionMiddleware> logger)
	{
		_logger = logger;
		_next = next;
	}

	public async Task Invoke(HttpContext httpContext)
	{
		try
		{
			await _next(httpContext);
		}
		catch (Exception ex)
		{
			_logger.LogError(ex, ex.Message);
			await HandleExceptionAsync(httpContext, ex);
		}
	}

	private static Task HandleExceptionAsync(HttpContext context, Exception exception)
	{
		context.Response.ContentType = "application/json";
		context.Response.StatusCode = (int)HttpStatusCode.InternalServerError;

		return context.Response.WriteAsync(new ErrorDetails()
		{
			StatusCode = context.Response.StatusCode,
			Message = exception.Message
		}.ToString());
	}
}

//result: 
// {
//   "statusCode": 500,
//   "message": "Error message"
// }
```
- Then you need to config **Middleware** in **Program.cs** file
- Example:
```csharp
app.UseMiddleware<ExceptionMiddleware>();
```

### 7. Start with a new api
#### 7.1 Make sure you have all models such as **RequestModel**, **ResponseModel**, **Entity**
- Example: 

```csharp
namespace ProjectName.Models.RequestModels
{
	public class RequestModel
	{
		public string Name { get; set; }
		public string Description { get; set; }
	}
}

namespace ProjectName.Models.ResponseModels
{
	public class ResponseModel
	{
		public int Id { get; set; }
		public string Name { get; set; }
		public string Description { get; set; }
	}
}


namespace ProjectName.Models.Entities
{
	public class Entity
	{
		public int Id { get; set; }
		public string Name { get; set; }
		public string Description { get; set; }
	}
}


// file: Models/Entities/Entity.cs
```

#### 7.2 Create a new service in **Services** folder
- Example:
```csharp
public class Service
{
	private readonly ProjectNameDbContext _context;

	public Service(ProjectNameDbContext context)
	{
		_context = context;
	}

	public async Task<ResponseModel> Get(int id)
	{
		var entity = await _context.Entity.FirstOrDefaultAsync(x => x.Id == id);
		if (entity == null)
		{
			throw new Exception("Entity not found");
		}
		return new ResponseModel()
		{
			Id = entity.Id,
			Name = entity.Name,
			Description = entity.Description
		};
	}
}
```

#### 7.3 Create a new controller in **Controller** folder
- Example:
```csharp
[Route("api/[controller]")]
[ApiController]
public class Controller : ControllerBase
{
	private readonly Service _service;

	public Controller(Service service)
	{
		_service = service;
	}

	[HttpGet("{id}")]
	public async Task<IActionResult> Get(int id)
	{
		var result = await _service.Get(id);
		return Ok(result);
	}
}
```
- Make sure you have to register **Service** in **Program.cs** file
- Example:
```csharp
services.AddScoped<Service>(); 
// or services.AddTransient<Service>();
// or services.AddSingleton<Service>();

//it depend on the situation of your project
```

### 7.4 Create a new test in **Test** folder
- Example:
```csharp
public class ServiceTest
{
	private readonly Service _service;

	public ServiceTest()
	{
		var options = new DbContextOptionsBuilder<ProjectNameDbContext>()
			.UseInMemoryDatabase(databaseName: "ProjectName")
			.Options;
		var context = new ProjectNameDbContext(options);
		_service = new Service(context);
	}

	[Fact]
	public async Task Get()
	{
		var result = await _service.Get(1);
		Assert.NotNull(result);
	}
}
```

### 8. Push to your repository
- If you use the task management tool like **Jira**, **Trello**, ... you need to create a new task with name is **ProjectName**
#### 8.1 When you receive a task
- When you was assigned a new feature or a bug, you need to create a new branch with name is **feature/task-name** or **bug/task-name**

#### 8.2 Commit your code to your local repository
- Example:
```bash
git add .
# you should use git status to check your files before commit
# and make sure you don't commit unnecessary files
# you have to commit with a template message like this
 you can use task id in your message like this
git commit -m "[TASK-1] Done a new feature"

#if in this task you have done yet but you want to commit your code
# you can use this message
git commit -m "[TASK-1] Done a new feature but not yet"

# if you have done a feature but you want to commit your code
# you can use this message
git commit -m "[TASK-1] Done a new feature and commit code"

# why you need to use a template message?
# because it will help you to know what you have done in this commit
# and it will help you to know what you have done in the past

git push origin feature/task-1
```

#### 8.3 Create a new pull request
- When you have done a feature or a bug, you need to create a new pull request with name is **[TASK-1] Done a new feature**
- Then you need to assign a reviewer for this pull request
- After that, you need to wait for the reviewer to review your code
- If the reviewer has any comments, you need to fix it
- If the reviewer has no comments, you can merge your code to **develop** branch

#### 8.4 Merge your code to develop branch
- When you have done a feature or a bug, you need to merge your code to **develop** branch
- Example:
```bash
git checkout develop
git pull origin develop
git merge feature/task-1
git push origin develop
```

#### 8.5 Create a new release
- When you have done a feature or a bug, you need to create a new release with name is **v1.0.0**
- Then you need to assign a reviewer for this release
- After that, you need to wait for the reviewer to review your code
- If the reviewer has any comments, you need to fix it
- If the reviewer has no comments, you can merge your code to **production** branch

#### 8.6 Merge your code to production branch
- When you have done a feature or a bug, you need to merge your code to **production** branch
- Example:
```bash
git checkout production
git pull origin production
git merge develop
git push origin production
```
**Note**: 
- You should not commit your code to **master** branch because it will make your repository unstable
- You should not commit your code to **production** branch because it will make your repository unstable
- Make sure you have to commit your code to **develop** branch before you create a new release and you have no conflicts when you merge your code to **production** branch from **develop** branch or from **feature** branch to **develop** branch
- And the name branch is **develop** and **production** is just an example, you can use any name for your branch

### 9. Deploy to your server
- You can use **Jenkins**, **TeamCity**, **Azure DevOps**, ... to deploy your code to your server
- You can use **Docker**, **Kubernetes**, ... to deploy your code to your server
- You can use **AWS**, **Azure**, **Google Cloud**, ... to deploy your code to your server
- You can use **Nginx**, **Apache**, ... to deploy your code to your server
- You can use **Linux**, **Windows**, ... to deploy your code to your server
- You can use **IIS**, **Nginx**, **Apache**, ... to deploy your code to your server
