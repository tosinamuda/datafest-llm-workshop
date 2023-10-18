import AppConfig from '@/config'
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import type { CareerAdvisor } from './types'

// Define a service using a base URL and expected endpoints
export const careerAdvisorApi = createApi({
  reducerPath: 'promptApi',
  baseQuery: fetchBaseQuery({ baseUrl: AppConfig.BASE_URL }),
  tagTypes: ["Industries"],
  endpoints: (builder) => ({
    generateIndustry: builder.query<string[], CareerAdvisor>({
      query: ({ ...career }: CareerAdvisor) => ({
        url: 'prompt/industry',
        params: career
      }),
      transformResponse: (response: { data: string[] }) => response.data,
      providesTags: ["Industries"]
    }),
  }),
})


export const { useLazyGenerateIndustryQuery } = careerAdvisorApi
