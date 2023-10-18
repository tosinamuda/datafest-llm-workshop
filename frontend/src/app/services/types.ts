import { z } from "zod";
export type CareerAdvisor = {
  course_of_study: string,
  career_interest?: string,
  limit: number
}


export const validationSchema = z.object({
  course_of_study: z.string().min(2, { message: "Enter Valid Course of Study" }),
  career_interest: z.string().optional(),
  limit: z.coerce.number().positive().optional().default(3)
})

export type ValidationSchema = z.infer<typeof validationSchema>;
