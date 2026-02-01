from fda_integration import OpenFDAClient

def main():
    client = OpenFDAClient()

	# Can change the drug name here to explore more drugs
    drug_name = "lisinopril"
    reactions = client.query_adverse_events(drug_name, limit=5)

	# Write into sample_output
    lines = [f"Top {len(reactions)} adverse reactions for {drug_name}:"]

    print(f"Top {len(reactions)} adverse reactions for {drug_name}:")
    for idx, (item, count) in enumerate(reactions, start=1):
        print(f"{idx}.{item} - {count} reports")
        lines.append(f"{idx}.{item} - {count} reports")
    output_text = "\n".join(lines)

    with open("sample_output.txt", "w", encoding="utf-8") as f:
        f.write(output_text)
	


if __name__ == "__main__":
    main()
