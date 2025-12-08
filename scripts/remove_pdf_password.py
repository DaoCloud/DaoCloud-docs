#!/usr/bin/env python3
"""
Simple utility to remove password (encryption) from a PDF using PyPDF2.

Usage:
  python3 remove_pdf_password.py /path/to/encrypted.pdf [/path/to/output.pdf]

If output path is omitted, a file with suffix "_no_password.pdf" will be created
next to the source file.
"""
import argparse
import os
import sys

import PyPDF2


def main():
    parser = argparse.ArgumentParser(description="Remove password/encryption from a PDF")
    parser.add_argument('source', help='Source PDF file (possibly encrypted)')
    parser.add_argument('output', nargs='?', help='Output PDF file path (optional)')
    args = parser.parse_args()

    source = args.source
    if not os.path.isfile(source):
        print(f"Source file does not exist: {source}")
        sys.exit(2)

    output = args.output or (os.path.splitext(source)[0] + '_no_password.pdf')

    try:
        with open(source, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            print(f"Is Encrypted: {reader.is_encrypted}")
            try:
                # Some PDFs may be decryptable with an empty password
                if reader.is_encrypted:
                    try:
                        reader.decrypt('')
                    except Exception:
                        # PyPDF2 may still be able to read certain files without explicit decryption
                        pass

                writer = PyPDF2.PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                with open(output, 'wb') as out_f:
                    writer.write(out_f)

            except Exception as e:
                print(f"Failed to write output PDF: {e}")
                sys.exit(1)

        print(f"Success: saved unencrypted PDF to {output}")
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
