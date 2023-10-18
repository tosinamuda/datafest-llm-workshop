import { SerializedError } from "@reduxjs/toolkit";
import { FetchBaseQueryError } from "@reduxjs/toolkit/query";
import { ButtonSkeleton, ErrorAlert } from "./";

type CareerAdvisorOuptutProps = {
  error?: FetchBaseQueryError | SerializedError;
  isLoading: boolean;
  industries?: string[];
};
const CareerAdvisorOutput = ({
  error,
  isLoading,
  industries,
}: CareerAdvisorOuptutProps) => {
  return (
    <div className="py-4 px-4">
      <div className="py-2 px-3">Industries</div>
      {error && <ErrorAlert />}
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
  );
};
export default CareerAdvisorOutput;
