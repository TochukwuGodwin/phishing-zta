"""Layered risk model and Zero Trust risk score from Section 5.3 of the report.
The numbers are ILLUSTRATIVE assumptions, not measurements."""

def p_comp(p_d, p_c, p_s, e_m):
    """Equation 3: probability that a recipient ends with a compromised account."""
    return p_d * p_c * p_s * (1 - e_m)

def expected_loss(n, p, l_avg):
    """Equation 4: E[L] = N * P_comp * L_avg."""
    return n * p * l_avg

def risk_score(r_u, r_d, r_c, w=(0.4, 0.3, 0.3)):
    """Equation 1: R = w_u*r_u + w_d*r_d + w_c*r_c (weights are assumptions)."""
    return w[0] * r_u + w[1] * r_d + w[2] * r_c

def decide(r_u, r_d, r_c, theta):
    return "grant" if risk_score(r_u, r_d, r_c) < theta else "step-up or deny"

if __name__ == "__main__":
    print("credentials captured per 1,000:", round(1000 * 0.9 * 0.08 * 0.07, 2))
    print("accounts taken over, no second factor:", round(1000 * p_comp(0.9, 0.08, 0.07, 0.0), 2))
    print("accounts taken over, E_m = 0.99:", round(1000 * p_comp(0.9, 0.08, 0.07, 0.99), 3))
    print(decide(0.2, 0.1, 0.1, 0.3), "|", decide(0.2, 0.9, 0.8, 0.3))
