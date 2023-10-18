import { useLazyGenerateIndustryQuery } from "@/app/services/career";
import { ValidationSchema, validationSchema } from "@/app/services/types";
import { zodResolver } from "@hookform/resolvers/zod";
import { SubmitHandler, useForm } from "react-hook-form";
import { CareerAdvisorForm, CareerAdvisorOutput } from "./components";

const CareerAdvisorView = () => {
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

  const onSubmit: SubmitHandler<ValidationSchema> = (data) =>
    generateIndustry(data);

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

            <CareerAdvisorForm
              register={register}
              handleSubmit={handleSubmit}
              onSubmit={onSubmit}
              errors={errors}
            />
          </div>

          <div className="lg:col-span-4 mt-10 lg:mt-0">
            <div className="w-full rounded-xl bg-slate-100 min-h-[200px] aspect-[9/7]">
              <CareerAdvisorOutput
                isLoading={isLoading}
                error={error}
                industries={industries}
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CareerAdvisorView;
