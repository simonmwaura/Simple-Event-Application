import {useState} from "react"
import {FiMail,FiLock,FiEye,FiEyeOff} from "react-icons/fi";

const Login = () =>{
    const[Email,setEmail]=useState("")
    const[Password,setPassword]=useState("")
    const[showPassword,setshowPassword]=useState(false)
    const HandleEmail=(event)=>{setEmail(event.target.value)}
    const HandlePassword=(event)=>{setPassword(event.target.value)}
    const PasswordVisibility=()=>{setshowPassword(!showPassword)}
    const HandleForm=(event)=>{
        event.preventDefault()
        console.log("Form Submitted",{Email,Password})
    }

    return (
    <section className="bg-blue-50 dark:bg-blue-900 min-h-screen flex items-center justify-center p-4">
        <div className="w-full max-w-md">
            <div className="bg-white rounded-xl shadow-lg dark:bg-blue-800 p-6 md:p-8">
                <div className="flex justify-center mb-6">
                    <div className="flex items-center">
                        <img className="w-12 h-12 mr-3" src="https://imgs.search.brave.com/gmf9R2Na0bQ-F6_AT30vfMxjZX7gBEk9WPy8PRJaOfo/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9sb2dv/LmNvbS9pbWFnZS1j/ZG4vaW1hZ2VzL2t0/czkyOHBkL3Byb2R1/Y3Rpb24vZWNhMjg4/YTY2MGZjMmIzODgz/YTk5ZTg2YWNhNTll/MTgxNGQyOTdlYi0z/NTR4MzQyLnBuZz93/PTEwODAmcT03MiZm/bT13ZWJw"
                        alt="Unforgettable Events logo"/>
                        <h1 className="text-blue-600 text-2xl font-bold">Unforgettable Events</h1>
                    </div>
                </div>
               <h1 className="text-xl font-bold text-center text-blue-600 dark:text-white mb-6">Log in to your account</h1>

            <div className="bg-blue-100 dark:bg-blue-700 rounded-lg p-6 mb-4">
                
                <form className="space-y-4" onSubmit={HandleForm}>
                <div>
                    <label htmlFor="email" className="block mb-1 text-sm font-medium text-blue-800 dark:text-blue-100">
                    Your email
                    </label>
                    <div className="relative">
                        <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                            <FiMail className="w-5 h-5 text-blue-500" />
                        </div>
                        <input type="email" name="email" value={Email} onChange={HandleEmail} className="bg-white border border-blue-200 text-blue-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 placeholder-blue-300 dark:bg-blue-600 dark:border-blue-500 dark:placeholder-blue-300 dark:text-white"
                        placeholder="name@example.com"required/>
                    </div>
                </div>

                <div>
                    <label htmlFor="password" className="block mb-1 text-sm font-medium text-blue-800 dark:text-blue-100">Password</label>
                    <div className="relative">
                        <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                             <FiLock className="w-5 h-5 text-blue-500" />
                        </div>
                        <input type={showPassword ? "text" : "password"}
                            value={Password} onChange={HandlePassword} name="password" placeholder="••••••••"
                            className="bg-white border border-blue-200 text-blue-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 pr-10 p-2.5 placeholder-blue-300 dark:bg-blue-600 dark:border-blue-500 dark:placeholder-blue-300 dark:text-white"required/>
                        <button type="button" className="absolute inset-y-0 right-0 flex items-center pr-3" onClick={PasswordVisibility}>
                        {showPassword ? (<FiEyeOff className="w-5 h-5 text-blue-500 hover:text-blue-600" />) : (<FiEye className="w-5 h-5 text-blue-500 hover:text-blue-600" />)}
                        </button>
                    </div>
                </div>

                <button type="submit" className="w-full text-white border hover:border-blue-500 hover:text-blue-700 bg-blue-600 hover:bg-blue-50 focus:ring-4 focus:outline-none  focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 transition-colors duration-200 dark:bg-blue-500 dark:hover:bg-blue-600">Sign in</button>
                </form>
            </div>

            <div className="flex flex-col items-center space-y-1">
                <a href="#" className="text-sm font-medium text-blue-600 hover:underline dark:text-blue-300">Forgot password?</a>
                <p className="text-sm text-blue-500 dark:text-blue-300">Don't have an account?{' '}
                   <a href="#" className="font-medium hover:underline">Sign up</a>
                </p>
            </div>
            </div>
        </div>
    </section>
    )
}
export default Login