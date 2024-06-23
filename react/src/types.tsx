export interface FormData {
  age: string;
  annual_income: string;
  monthly_inhand_salary: string;
  interest_rate: string;
  num_of_loan: string;
  delay_from_due_date: string;
  changed_credit_limit: string;
  num_credit_inquiries: string;
  credit_mix: string;
  outstanding_debt: string;
  credit_utilization_ratio: string;
  payment_of_min_amount: string;
  total_emi_per_month: string;
  payment_behaviour: string;
}

export const initialFormData: FormData = {
  age: '',
  annual_income: '',
  monthly_inhand_salary: '',
  interest_rate: '',
  num_of_loan: '',
  delay_from_due_date: '',
  changed_credit_limit: '',
  num_credit_inquiries: '',
  credit_mix: '',
  outstanding_debt: '',
  credit_utilization_ratio: '',
  payment_of_min_amount: '',
  total_emi_per_month: '',
  payment_behaviour: '',
};