import { useLazyGenerateIndustryQuery } from "@/app/services/career";
import { ValidationSchema, validationSchema } from "@/app/services/types";
import { zodResolver } from "@hookform/resolvers/zod";
import { SubmitHandler, useForm } from "react-hook-form";

const Job = () => {
  const [generateIndustry, { isLoading, error, data: industries }] =
    useLazyGenerateIndustryQuery();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ValidationSchema>({
    resolver: zodResolver(validationSchema),
    mode: "onTouched",
  });

  const onSubmit: SubmitHandler<ValidationSchema> = (data) => {
    console.log(data);
    generateIndustry(data);
  };

  return (
    <section className="bg-white ">
      <div className="max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8 pt-6 lg:pt-10">
        <div className="grid lg:grid-cols-7 lg:gap-x-8 xl:gap-x-12 lg:items-center">
          <div className="lg:col-span-3">
            <h1 className="block text-3xl font-bold text-gray-800 sm:text-4xl md:text-5xl lg:text-6xl dark:text-white">
              Discover your career options
            </h1>
            <p className="mt-3 text-lg text-gray-800 dark:text-gray-400">
              Explore career paths aligned with your Field of Study or
              Interests.
            </p>

            <form className="mt-5 lg:mt-8" onSubmit={handleSubmit(onSubmit)}>
              <div className="grid grid-cols-1 lg:grid-cols-2 items-center gap-6">
                <div>
                  <div className="mb-8">
                    <label
                      htmlFor="name"
                      className="block text-sm font-semibold mb-1 text-gray-600"
                    >
                      Course of Study<small>*</small>
                    </label>
                    <input
                      className="py-3 px-4 block w-full xl:min-w-[18rem] border-gray-200 shadow-sm rounded-md focus:z-10 focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
                      placeholder="Enter your course of study"
                      defaultValue="Accounting"
                      {...register("course_of_study")}
                    />
                  </div>
                  <div className="mb-8">
                    <label
                      htmlFor="name"
                      className="block text-sm font-semibold mb-1 text-gray-600"
                    >
                      Other Career Interest
                    </label>
                    <input
                      className="py-3 px-4 block w-full xl:min-w-[18rem] border-gray-200 shadow-sm rounded-md focus:z-10 focus:border-blue-500 focus:ring-blue-500 dark:bg-slate-900 dark:border-gray-700 dark:text-gray-400"
                      placeholder="Enter Your Career Interest"
                      defaultValue="None"
                      {...register("career_interest")}
                    />
                  </div>
                </div>
              </div>
              <div className="mt-4 grid gap-3 w-full sm:inline-flex">
                <button
                  type="submit"
                  className="inline-flex justify-center items-center gap-x-3 text-center bg-blue-600 hover:bg-blue-700 border border-transparent text-sm lg:text-base text-white font-medium rounded-md focus:outline-none focus:ring-2 focus:ring-blue-600 focus:ring-offset-2 focus:ring-offset-white transition py-3 px-4 dark:focus:ring-offset-gray-800"
                >
                  Advise Me
                  <svg
                    className="w-2.5 h-2.5"
                    width="16"
                    height="16"
                    viewBox="0 0 16 16"
                    fill="none"
                  >
                    <path
                      d="M5.27921 2L10.9257 7.64645C11.1209 7.84171 11.1209 8.15829 10.9257 8.35355L5.27921 14"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                    />
                  </svg>
                </button>
              </div>
            </form>
          </div>

          <div className="lg:col-span-4 mt-10 lg:mt-0">
            {/*        <img
              className="w-full rounded-xl"
              src="https://images.unsplash.com/photo-1665686376173-ada7a0031a85?ixlib=rb-4.0.3&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=900&amp;h=700&amp;q=80"
              alt="Image Description"
            /> */}
            <div className="w-full rounded-xl bg-slate-100 min-h-[200px] aspect-[9/7]">
              <div className="py-4 px-4">
                <div className="py-2 px-3">Industries</div>
                {isLoading && (
                  <div className="py-1 px-3">
                    <ButtonSkeleton />
                  </div>
                )}
                {industries?.map((industry) => (
                  <button
                    key={industry}
                    className="rounded-full bg-blue-500/10 text-blue-500 font-semibold py-1 px-2 mx-3 my-2 md:my-0 text-sm"
                  >
                    {industry}
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Job;

const ButtonSkeleton = () => {
  return (
    <div role="status" className="space-y-2.5 animate-pulse max-w-lg">
      <div className="flex items-center w-full space-x-2">
        <div className="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-32"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full"></div>
      </div>
      <div className="flex items-center w-full space-x-2 max-w-[480px]">
        <div className="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-full"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24"></div>
      </div>
      <div className="flex items-center w-full space-x-2 max-w-[400px]">
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full"></div>
        <div className="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-80"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full"></div>
      </div>
      <div className="flex items-center w-full space-x-2 max-w-[480px]">
        <div className="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-full"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24"></div>
      </div>
      <div className="flex items-center w-full space-x-2 max-w-[440px]">
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-32"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-24"></div>
        <div className="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-full"></div>
      </div>
      <div className="flex items-center w-full space-x-2 max-w-[360px]">
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full"></div>
        <div className="h-2.5 bg-gray-200 rounded-full dark:bg-gray-700 w-80"></div>
        <div className="h-2.5 bg-gray-300 rounded-full dark:bg-gray-600 w-full"></div>
      </div>
      <span className="sr-only">Loading...</span>
    </div>
  );
};
